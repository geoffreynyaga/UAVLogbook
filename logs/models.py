from django.db import models

# Create your models here.
class BaseLog(models.Model):
    """Model definition for BaseLog."""

    # TODO: Define fields here

    flight_time = models.FloatField()
    location_name = models.CharField(max_length=50, blank=True, null=True)
    aircraft = models.CharField(max_length=50)
    pilot_name = models.CharField(max_length=50)
    co_pilot_name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for BaseLog."""

        verbose_name = "BaseLog"
        verbose_name_plural = "BaseLogs"

    def __str__(self):
        """Unicode representation of BaseLog."""
        pass

    def save(self):
        """Save method for BaseLog."""
        pass

    def get_absolute_url(self):
        """Return absolute url for BaseLog."""
        return ""

    # TODO: Define custom methods here


class EbeeClassicLogs(models.Model):
    """Model definition for EbeeClassicLogs."""

    # TODO: Define fields here
    log_id = models.CharField(
        max_length=40,
    )
    vehicle_sn = models.CharField(max_length=12)
    color = models.CharField(max_length=7)
    begin_date = models.CharField(max_length=20)
    firmware_version = models.CharField(max_length=70)
    total_flight_count = models.IntegerField()
    total_flight_duration = models.FloatField()
    home_lat = models.FloatField()
    home_lon = models.FloatField()
    start_lat = models.FloatField()
    start_lon = models.FloatField()
    end_lat = models.FloatField()
    end_lon = models.FloatField()
    cam_id = models.IntegerField()
    duration = models.FloatField()
    ground_distance = models.FloatField()
    mean_wind_speed = models.FloatField()
    max_wind_speed = models.FloatField()
    max_temperature = models.FloatField()
    min_altitude = models.FloatField()
    max_altitude = models.FloatField()
    max_height = models.FloatField()
    max_dist = models.FloatField()
    working_area_radius = models.IntegerField()
    working_area_ceiling = models.IntegerField()
    begin_battery_voltage = models.FloatField()
    end_battery_voltage = models.FloatField()
    min_return_to_home_ratio = models.FloatField()
    link_quality = models.FloatField()
    landing_type = models.IntegerField()
    mission_area = models.TextField()
    mission_param = models.TextField()
    flight_param = models.TextField()
    photo_count = models.IntegerField()
    log_file = models.CharField(max_length=40)
    bbx_file = models.CharField(max_length=70)
    base_logFile = models.CharField(max_length=40)
    gps_info = models.CharField(max_length=50)
    correction_source = models.IntegerField()

    class Meta:
        """Meta definition for EbeeClassicLogs."""

        verbose_name = "EbeeClassicLogs"
        verbose_name_plural = "EbeeClassicLogs"

    def __str__(self):
        """Unicode representation of EbeeClassicLogs."""
        pass

    def save(self):
        """Save method for EbeeClassicLogs."""
        pass

    def get_absolute_url(self):
        """Return absolute url for EbeeClassicLogs."""
        return ""

    # TODO: Define custom methods here
