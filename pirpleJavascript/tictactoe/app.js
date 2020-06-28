// Get UI elements
const board = document.querySelector('.play-area');

let squares = Array(9).fill(null);
let winner = null;
let xIsNext = true;
let endMessage = '';
let gameOver = false;

const getPlayer = () => {
  return xIsNext ? 'X' : 'O';
};

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

const showModal = () => {
  document.getElementById('myModal').style.display = 'block';
};

const hideModal = () => {
  document.getElementById('myModal').style.display = 'none';
};

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
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName('close')[0];

// When the user clicks on <span> (x), close the modal
span.onclick = () => {
  hideModal();
  resetBoard();
};

// When the user clicks anywhere outside of the modal, close it
// window.onclick = function (event) {
//   if (event.target == modal) {
//     modal.style.display = 'none';
//   }
// };

// const player = 'O';
// const computer = 'X';

// let board_full = false;
// let play_board = ['', '', '', '', '', '', '', '', ''];

// const board_container = document.querySelector('.play-area');

// const winner_statement = document.getElementById('winner');

// check_board_complete = () => {
//   let flag = true;
//   play_board.forEach((element) => {
//     if (element != player && element != computer) {
//       flag = false;
//     }
//   });
//   board_full = flag;
// };

// const check_line = (a, b, c) => {
//   return (
//     play_board[a] == play_board[b] &&
//     play_board[b] == play_board[c] &&
//     (play_board[a] == player || play_board[a] == computer)
//   );
// };

// const check_match = () => {
//   for (i = 0; i < 9; i += 3) {
//     if (check_line(i, i + 1, i + 2)) {
//       return play_board[i];
//     }
//   }
//   for (i = 0; i < 3; i++) {
//     if (check_line(i, i + 3, i + 6)) {
//       return play_board[i];
//     }
//   }
//   if (check_line(0, 4, 8)) {
//     return play_board[0];
//   }
//   if (check_line(2, 4, 6)) {
//     return play_board[2];
//   }
//   return '';
// };

// const check_for_winner = () => {
//   let res = check_match();
//   if (res == player) {
//     winner.innerText = 'Winner is player!!';
//     winner.classList.add('playerWin');
//     board_full = true;
//   } else if (res == computer) {
//     winner.innerText = 'Winner is computer';
//     winner.classList.add('computerWin');
//     board_full = true;
//   } else if (board_full) {
//     winner.innerText = 'Draw!';
//     winner.classList.add('draw');
//   }
// };

// const render_board = () => {
//   board_container.innerHTML = '';
//   play_board.forEach((e, i) => {
//     board_container.innerHTML += `<div id="block_${i}" class="block" onclick="addPlayerMove(${i})">${play_board[i]}</div>`;
//     if (e == player || e == computer) {
//       document.querySelector(`#block_${i}`).classList.add('occupied');
//     }
//   });
// };

// const game_loop = () => {
//   render_board();
//   check_board_complete();
//   check_for_winner();
// };

// const addPlayerMove = (e) => {
//   if (!board_full && play_board[e] == '') {
//     play_board[e] = player;
//     game_loop();
//     addComputerMove();
//   }
// };

// const addComputerMove = () => {
//   if (!board_full) {
//     do {
//       selected = Math.floor(Math.random() * 9);
//     } while (play_board[selected] != '');
//     play_board[selected] = computer;
//     game_loop();
//   }
// };

// const reset_board = () => {
//   play_board = ['', '', '', '', '', '', '', '', ''];
//   board_full = false;
//   winner.classList.remove('playerWin');
//   winner.classList.remove('computerWin');
//   winner.classList.remove('draw');
//   winner.innerText = '';
//   render_board();
// };

// //initial render
// render_board();
