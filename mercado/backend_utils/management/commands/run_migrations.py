from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run migrations and log results'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Running migrations...'))
            call_command('migrate', '--noinput', verbosity=2)
            self.stdout.write(self.style.SUCCESS('Migrations completed successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error running migrations: {str(e)}'))
