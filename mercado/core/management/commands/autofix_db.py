import time
import sys
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError, ProgrammingError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Detects and fixes database connection and migration issues automatically on Render'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Starting Auto-Fix Database Script...'))

        # 1. Wait for Database Connection
        self.wait_for_db()

        # 2. Attempt Migrations with Auto-Fix Logic
        self.run_safe_migrations()

        self.stdout.write(self.style.SUCCESS('Auto-Fix Script Completed Successfully.'))

    def wait_for_db(self):
        """Waits for the database to be available."""
        self.stdout.write('Checking database connection...')
        db_conn = None
        for i in range(30):  # Wait up to 30 seconds
            try:
                db_conn = connections['default']
                db_conn.cursor()
                self.stdout.write(self.style.SUCCESS('Database is available!'))
                return
            except OperationalError:
                self.stdout.write(f'Database unavailable, waiting 1 second... ({i+1}/30)')
                time.sleep(1)
        
        self.stdout.write(self.style.ERROR('Could not connect to database after 30 seconds.'))
        sys.exit(1)

    def run_safe_migrations(self):
        """Runs migrations and handles common inconsistencies."""
        self.stdout.write('Attempting to apply migrations...')
        
        try:
            # Try normal migration first
            call_command('migrate', interactive=False)
            self.stdout.write(self.style.SUCCESS('Migrations applied successfully.'))
        except (OperationalError, ProgrammingError) as e:
            self.stdout.write(self.style.WARNING(f'Standard migration failed: {e}'))
            self.stdout.write(self.style.WARNING('Attempting to fix by faking initial migrations...'))
            
            try:
                # If tables exist but migrations are missing, --fake-initial helps
                call_command('migrate', fake_initial=True, interactive=False)
                self.stdout.write(self.style.SUCCESS('Fixed using --fake-initial!'))
            except Exception as e2:
                self.stdout.write(self.style.ERROR(f'Failed to auto-fix migrations: {e2}'))
                # If this fails, we might have a serious issue. 
                # But we won't do anything destructive automatically without more info.
                sys.exit(1)
        except Exception as e:
             self.stdout.write(self.style.ERROR(f'Unexpected error during migration: {e}'))
             sys.exit(1)
