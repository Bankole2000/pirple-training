/*
 * FileName: song.js V1.0
 * Author: Bankole Esan
 * Description: Pirple.com JavaScript Homework #1
 * Task: Variables for attributes of favorite Song
 */

const songTitle = 'Wa Mpaleha'; // Title of the song
const artist = 'Lira'; // Recording Artist
const genre = 'R & B'; // Genre or Category of the song
const yearReleased = 2008; // Year released
const recordLabel = 'Sony Music'; // Record label song was released under
const albumName = 'Soul in Mind'; // Album where song first featured
const albumPriceInDollars = 9.99; // Album price in dollars
const albumIsInStoresNow = true; // Album available in stores?
const artistIsOnTour = false; // Artist on tour?
// Album or song streaming services
const streamingServices = [
  {
    service: 'spotify',
    url: 'https://open.spotify.com/playlist/3wptUXmGGVVZlQwLBnvzPI',
  },
  {
    service: 'apple',
    url: 'https://itunes.apple.com/cy/music-video/wa-mpaleha/448158838',
  },
  {
    service: 'deezer',
    url: 'https://www.deezer.com/en/track/110958918',
  },
];
// Names of Tracks on album
const albumTracks = [
  'Wa Mpaleha',
  'Soul in Mind',
  'Gotta Let go',
  'Rise Again',
  'Crush',
  'Something inside so strong',
];
// Details of specific track
const trackDetails = {
  trackNumber: 1, // Song track number on album
  durationInSeconds: 204, // Length of song in seconds
  getDurationInMinutes: function () {
    return `${Math.floor(this.durationInSeconds / 60)}m ${
      this.durationInSeconds % 60
    }s`;
  },
  fileFormat: 'mp3', // File Format
  hasMusicVideo: true, // if song has music video
  videoURL: 'https://youtu.be/SDi4gUYHENE', // Url to music video
  getVideoURL: function () {
    return this.hasMusicVideo ? this.videoURL : 'none';
  },
  sizeInMB: 9.09, // Size of song on disk in MegaBytes
  getSizeInKB: function () {
    return this.sizeInMB * 1024;
  },
};
const countryOfFirstRelease = 'South Africa';

console.log(`Song Title: ${songTitle}`);
console.log(`Artist: ${artist}`);
console.log(`Genre: ${genre}`);
console.log(`Album name: ${albumName}`);
console.log(`Year: ${yearReleased}`);
console.log(`Label: ${recordLabel}`);
console.log(`Country Released in: ${countryOfFirstRelease}`);
console.log(`Album price: $${albumPriceInDollars}`);
console.log(`In Stores Now: ${albumIsInStoresNow}`);
console.log(`Artist On Tour: ${artistIsOnTour}`);
console.log(`Album Tracks: ${albumTracks}`);
console.table(albumTracks);
console.log(`Streaming Services: ${streamingServices}`);
console.table(streamingServices);
console.log(`Track Details: ${trackDetails}`);
console.table(trackDetails);
console.log(`Track Number: ${trackDetails.trackNumber}`);
console.log(`Track Duration in Seconds: ${trackDetails.durationInSeconds}s`);
console.log(
  `Track Duration in Minutes: ${trackDetails.getDurationInMinutes()}`
);
console.log(`File Format: ${trackDetails.fileFormat}`);
console.log(`Track Has Music Video: ${trackDetails.hasMusicVideo}`);
console.log(`Music Video URL: ${trackDetails.getVideoURL()}`);
console.log(`Size In MB: ${trackDetails.sizeInMB} MB`);
console.log(`Size In KB: ${trackDetails.getSizeInKB()} KB`);
