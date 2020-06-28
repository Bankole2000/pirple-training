// Get UI elements
const board = document.querySelector('.play-area');

// Game variables
let squares = Array(9).fill(null);
let winner = null;
let xIsNext = true;
let endMessage = '';
let gameOver = false;

// Switch players every turn
const getPlayer = () => {
  return xIsNext ? 'X' : 'O';
};

// Make Move in box on click event
const makeMove = (idx) => {
  if (squares[idx] == null) {
    player = getPlayer();
    squares.splice(idx, 1, player);
    xIsNext = !xIsNext;
    console.log(xIsNext);
    winner = calculateWinner();
    return true;
  } else {
    return false;
  }
};

// Reset board on reset button click or after game over/game won
const resetBoard = () => {
  squares = Array(9).fill(null);
  winner = null;
  xIsNext = true;
  endMessage = '';
  gameOver = false;
  spaces = document.querySelectorAll('.block');
  document.getElementById('myModal').style.display = 'none';
  spaces.forEach((space) => {
    space.innerHTML = '';
  });
};

// show modal function
const showModal = () => {
  document.getElementById('myModal').style.display = 'block';
};

// Hide modal function
const hideModal = () => {
  document.getElementById('myModal').style.display = 'none';
};

// Calculate winner every turn
const calculateWinner = () => {
  const lines = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 4, 6],
    [2, 5, 8],
    [3, 4, 5],
    [6, 7, 8],
  ];

  for (i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (a != null && b != null && c != null) {
      if (
        squares[a] &&
        squares[b] === squares[c] &&
        squares[a] === squares[c]
      ) {
        console.log(`Winner is ${squares[a]}`);
        document.querySelector(
          '.message'
        ).innerHTML = `👍Winner is ${squares[a]}!`;
        showModal();
        gameOver = true;
        return squares[a];
      }
    }
  }
  return null;
};

// Game event loop
board.addEventListener('click', (e) => {
  if (e.target.classList.contains('block')) {
    let boxNumber = e.target.id.split('_')[1];
    let icon = getPlayer();
    if (makeMove(boxNumber)) {
      document.querySelector(`#block_${boxNumber}`).innerHTML = icon;
      if (!xIsNext) {
        document.querySelector(`#block_${boxNumber}`).style.color = 'red';
      } else {
        document.querySelector(`#block_${boxNumber}`).style.color = 'black';
      }
      if (squares.indexOf(null) == -1) {
        console.log('game over');
        document.querySelector('.message').innerHTML = `Cat's Game🐱! (Draw)`;
        showModal();
        gameOver = true;
      }
    } else {
      console.log("can't move there");
    }
  }
});

// Get the modal
const modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
const span = document.getElementsByClassName('close')[0];

// When the user clicks on <span> (x), close the modal
span.onclick = () => {
  hideModal();
  resetBoard();
};
