from webexteamssdk import WebexTeamsAPI
import sys

TEAMS_TOKEN = ''

teamsapi = WebexTeamsAPI(access_token=TEAMS_TOKEN)

createdroom = teamsapi.rooms.create(title="Devnet High 2020")

if createdroom.title == "Devnet High 2020":
    print("Room successfully created, sending test message")
    teamsapi.messages.create(roomId=createdroom.id, text="Hello? Is anyone actually in this class?")
else:
    print("error, room was not created, please try again")
    exit

input("\n Paused, press enter and the room will be deleted.")
teamsapi.rooms.delete(createdroom.id)