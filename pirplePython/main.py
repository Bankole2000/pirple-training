"""
FileName: main.py V1.0
Author: Bankole Esan
Description: Pirple.com Python Homework #1
Task: Variables for attributes of favorite Song
"""

SongTitle = "Wa Mpaleha"  # Title of the song
Artist = "Lira"  # Recording Artist
Genre = "R & B"  # Genre or Category of the song
DurationInSeconds = 204  # Length of song in seconds
# Length of song in minutes
DurationInMinutes = f"{ int((DurationInSeconds / 60) - ((DurationInSeconds % 60) / 60)) }:{ DurationInSeconds % 60 }"
Album = "Soul in Mind"  # Album where song first featured
TrackNumber = 1  # Song track number on album
CountryOfFirstRelease = "South Africa"  # Any Featured artists
YearReleased = 2008  # Year released
RecordLabel = "Sony Music"  # Record label song was released under
Mp3FileSizeInMB = 9.09  # Size of song on disk in MegaBytes
Mp3FileSizeInKB = Mp3FileSizeInMB * 1024  # Size of song on disk in KiloBytes
InStoresNow = True
# print(f"Title: {SongTitle}")
# print(f"Artist: {Artist}")
# print(f"Genre: {Genre}")
# print(f"Duration in Seconds: {DurationInSeconds}")
# print(f"Duration in Minutes: {DurationInMinutes}")
# print(f"Album name: {Album}")
# print(f"Track Number: {TrackNumber}")
# print(f"Country of Release: {CountryOfFirstRelease}")
# print(f"Year: {YearReleased}")
# print(f"Label: {RecordLabel}")
# print(f"Size in MB: {Mp3FileSizeInMB} MB")
# print(f"Size in KB: {Mp3FileSizeInKB} KB")
