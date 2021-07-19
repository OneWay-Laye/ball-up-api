from django.db import models

from django.contrib.auth import get_user_model

class MeetUp(models.Model):
    """This will be the join table for players and location"""
    scheduled = models.DateField()
    player_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
    related_name="attendingMeetup")
    park_id = models.ForeignKey('Park', on_delete=models.CASCADE ,
    related_name="meetupLocation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="ownedMeetup"
    )

    # joined_players = models.ManyToMany(
    #     get_user_model(),
    #   )


    def __str__(self):
        return f"{self.scheduled}"
