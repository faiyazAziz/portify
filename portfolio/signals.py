# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Template
from selenium import webdriver
from django.core.files import File
import os
import time
from django.conf import settings

@receiver(post_save, sender=Template)
def capture_screenshot(sender, instance, created, **kwargs):
    if created:
        url = f"http://127.0.0.1:8000/{instance.uid}"
        screenshot_path = os.path.join(settings.MEDIA_ROOT, f"{instance.name}.png")

        # Set up the Selenium WebDriver
        driver = webdriver.Chrome()
        try:
            driver.get(url)
            # Give the page some time to load
            time.sleep(2)
            # Save screenshot
            driver.save_screenshot(screenshot_path)

            # Save the screenshot to the model instance
            with open(screenshot_path, 'rb') as f:
                instance.screenshot.save(f'{instance.user.username}{instance.name}.png', File(f), save=False)

            instance.save()
        finally:
            driver.quit()
            if os.path.exists(screenshot_path):
                os.remove(screenshot_path)
