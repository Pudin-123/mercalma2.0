from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from mercado.market.models import Product

class Command(BaseCommand):
    help = 'Create default groups: buyer, seller, admin and assign basic permissions'

    def handle(self, *args, **options):
        buyer, _ = Group.objects.get_or_create(name='buyer')
        seller, _ = Group.objects.get_or_create(name='seller')
        admin_grp, _ = Group.objects.get_or_create(name='admin')

        ct = ContentType.objects.get_for_model(Product)
        perms = Permission.objects.filter(content_type=ct)
        for p in perms:
            if p.codename in ('add_product','change_product','delete_product'):
                seller.permissions.add(p)
                admin_grp.permissions.add(p)

        self.stdout.write(self.style.SUCCESS('Groups buyer, seller, admin created (permissions assigned to seller/admin).'))
