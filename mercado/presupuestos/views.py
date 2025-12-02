import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from presupuestos.models import Presupuesto
from presupuestos.utils import enviar_a_telegram
from django.contrib.auth.models import User
from django.conf import settings
from presupuestos.models import Presupuesto, TelegramLog
from django.shortcuts import render

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        message = data.get("message", {})
        chat = message.get("chat", {})
        chat_id = str(chat.get("id"))
        text = message.get("text", "")

        print("📩 LLEGÓ MENSAJE DE TELEGRAM:", data)

        try:
            # --- /listar ---
            if text.startswith("/listar"):
                presupuestos = Presupuesto.objects.order_by("-creado_en")[:5]
                respuesta = "\n".join(
                    [f"📦 {p.producto} - {p.email}" for p in presupuestos]
                ) or "No hay presupuestos."
                enviar_a_telegram(respuesta, chat_id)

            # --- /presupuesto <id> ---
            elif text.startswith("/presupuesto"):
                try:
                    _, pid = text.split()
                    p = Presupuesto.objects.get(id=int(pid))
                    respuesta = (
                        f"📦 Producto: {p.producto}\n"
                        f"📧 Email: {p.email}\n"
                        f"📝 {p.mensaje}\n"
                        f"⏰ {p.creado_en.strftime('%d-%m-%Y %H:%M')}"
                    )
                except Exception:
                    respuesta = "❌ ID inválido o presupuesto no encontrado."
                enviar_a_telegram(respuesta, chat_id)

            # --- /usuarios ---
            elif text.startswith("/usuarios"):
                usuarios = User.objects.order_by("-date_joined")[:5]
                print("Usuarios encontrados:", list(User.objects.all().values_list("username", flat=True)))
                if usuarios.exists():
                    for u in usuarios:
                        texto = f"👤 {u.username} ({u.email or 'sin email'})"
                        # botón opcional para abrir el admin
                        url_admin = f"{settings.SITE_URL}/admin/auth/user/{u.id}/change/".strip()
                        buttons = [[{"text": "🔗 Ver en Admin", "url": url_admin}]]
                        enviar_a_telegram(texto, chat_id, buttons=buttons)
                        print("➡️ Enviando mensaje a Telegram:", texto)

                else:
                    enviar_a_telegram("No hay usuarios registrados.", chat_id)

            # --- Comando desconocido ---
            else:
                enviar_a_telegram("Comandos: /listar, /presupuesto <id>, /usuarios", chat_id)

        except Exception as e:
            print("⚠️ ERROR EN TELEGRAM WEBHOOK:", e)
            enviar_a_telegram(f"⚠️ Error: {str(e)}", chat_id)

        return JsonResponse({"ok": True})
    
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        message = data.get("message", {})
        chat_id = str(message.get("chat", {}).get("id"))
        text = message.get("text", "")
        username = chat.get("username") or chat.get("first_name") or "Desconocido"
        chat = message.get("chat", {})


        # Guardamos log en la BD
        TelegramLog.objects.create(
            chat_id=chat_id,
            username=username,
            mensaje=text,
        )
        print("📩 LLEGÓ MENSAJE DE TELEGRAM:", data)

    return JsonResponse({"error": "Método no permitido"}, status=405)

def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.all().order_by("-creado_en")
    ultimo_log = TelegramLog.objects.order_by("-recibido_en").first()
    return render(request, "presupuestos/lista.html", {
        "presupuestos": presupuestos,
        "ultimo_log": ultimo_log,
    })

def dashboard(request):
    presupuestos = Presupuesto.objects.order_by('-creado_en')[:10]
    return render(request, 'presupuestos/dashboard.html', {'presupuestos': presupuestos})


