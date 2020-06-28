// function generateUUID() {
//   // Public Domain/MIT
//   var d3 = Date.now(); // Use this as d
//   var d = new Date().getTime(); //Timestamp
//   // var d2 = (performance && performance.now && performance.now() * 1000) || 0; //Time in microseconds since page-load or 0 if unsupported
//   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
//     var r = Math.random() * 16; //random number between 0 and 16
//     if (d > 0) {
//       //Use timestamp until depleted
//       r = (d + r) % 16 | 0;
//       d = Math.floor(d / 16);
//     } else {
//       //Use microseconds since page-load if supported
//       r = (d2 + r) % 16 | 0;
//       d2 = Math.floor(d2 / 16);
//     }
//     return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16);
//   });
// }

// generateUUID();

const createUUID = () => {
  strLength = 20;
  strLength = typeof strLength == 'number' && strLength > 0 ? strLength : false;
  if (strLength) {
    // define all possible characters that could go into a string
    const possibleCharacters = 'abcdefghijklmnopqrstuvwxyz0123456789';

    // Start the final string
    let str = '';
    for (i = 1; i <= strLength - 13; i++) {
      // Get a random character and append to final string
      const randomCharacter = possibleCharacters.charAt(
        Math.floor(Math.random() * possibleCharacters.length)
      );
      str += randomCharacter;
    }
    return (str += `-${Date.now().toString()}`);
  } else {
    return false;
  }
};

console.log(createUUID());
