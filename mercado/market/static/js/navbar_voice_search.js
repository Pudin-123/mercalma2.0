document.addEventListener('DOMContentLoaded', function() {
  console.log('navbar_voice_search.js cargado');
  const supportInfo = {
    SpeechRecognition: !!window.SpeechRecognition,
    webkitSpeechRecognition: !!window.webkitSpeechRecognition,
    userAgent: navigator.userAgent
  };
  console.log('SpeechRecognition support: ', supportInfo);
  const voiceBtn = document.getElementById('navbar-voice-search-btn');
  const searchInput = document.getElementById('navbar-search-input');
  // Añadir burbuja de debug visible para confirmar que el script está activo
  try {
    let dbg = document.getElementById('voice-debug-bubble');
    if (!dbg) {
      dbg = document.createElement('div');
      dbg.id = 'voice-debug-bubble';
      dbg.style.position = 'fixed';
      dbg.style.bottom = '12px';
      dbg.style.left = '12px';
      dbg.style.padding = '6px 10px';
      dbg.style.background = 'rgba(255,193,7,0.95)';
      dbg.style.color = '#111';
      dbg.style.borderRadius = '6px';
      dbg.style.zIndex = 99999;
      dbg.style.fontSize = '12px';
      dbg.textContent = 'Voice script: cargado — support: ' + (supportInfo.SpeechRecognition || supportInfo.webkitSpeechRecognition ? 'OK' : 'NO');
      document.body.appendChild(dbg);
    }
  } catch (e) {
    console.warn('No se pudo crear bubble debug', e);
  }
  if (voiceBtn) {
    if (window.SpeechRecognition || window.webkitSpeechRecognition) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      const recognition = new SpeechRecognition();
      recognition.lang = 'es-ES';
      recognition.continuous = false;
      recognition.interimResults = false;

      voiceBtn.addEventListener('click', function() {
        console.log('navbar voice button clicked');
        console.log('supportInfo on click:', supportInfo);
        const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: intentando iniciar...';
        voiceBtn.classList.add('active');
        voiceBtn.innerHTML = '<i class="bi bi-mic-fill text-danger"></i>';
        console.log('calling recognition.start()...');
        try {
          // Primero intentamos pedir permiso explícita y abrir el stream de audio
          if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            console.log('Solicitando permiso con getUserMedia...');
            navigator.mediaDevices.getUserMedia({ audio: true })
              .then(stream => {
                console.log('getUserMedia: permiso concedido, iniciando recognition...');
                try { recognition.start(); } catch (e) { console.error('Error starting recognition after getUserMedia:', e); alert('Error al iniciar reconocimiento: '+e.message); }
                // cerramos el stream inmediatamente (SpeechRecognition usa el micrófono por su cuenta)
                try { stream.getTracks().forEach(t=>t.stop()); } catch(e){}
              })
              .catch(err => {
                console.error('getUserMedia error', err);
                alert('No se pudo acceder al micrófono: ' + (err && err.message ? err.message : err));
                const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: permiso denegado';
              });
          } else {
            console.log('No hay getUserMedia, llamando recognition.start() directamente');
            recognition.start();
          }
        } catch (e) {
          console.error('Error starting recognition:', e);
          alert('No se pudo iniciar el reconocimiento de voz: ' + e.message);
          const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: error al iniciar';
        }
      });

      recognition.onstart = function() { console.log('recognition.onstart'); const dbg=document.getElementById('voice-debug-bubble'); if(dbg) dbg.textContent='Voice: escuchando...'; };
      recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        searchInput.value = transcript;
        voiceBtn.classList.remove('active');
        voiceBtn.innerHTML = '<i class="bi bi-mic"></i>';
        const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: resultado recibido';
      };
      recognition.onnomatch = function() { console.log('recognition.onnomatch'); const dbg=document.getElementById('voice-debug-bubble'); if(dbg) dbg.textContent='Voice: no match'; };
      recognition.onerror = function(err) {
        console.error('recognition.onerror', err);
        voiceBtn.classList.remove('active');
        voiceBtn.innerHTML = '<i class="bi bi-mic"></i>';
        alert('Error al reconocer la voz. Intenta de nuevo.');
        const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: error';
      };
      recognition.onend = function() {
        voiceBtn.classList.remove('active');
        voiceBtn.innerHTML = '<i class="bi bi-mic"></i>';
        const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: inactivo';
      };
    } else {
      voiceBtn.addEventListener('click', function() {
        console.log('voice not supported click');
        alert('La búsqueda por voz no está soportada en este navegador. Usa Google Chrome o Edge.');
        const dbg = document.getElementById('voice-debug-bubble'); if (dbg) dbg.textContent = 'Voice: no soportado en navegador';
      });
    }
  }
});
