// start / restart game button
var startBtn = document.querySelector("#b");

// grabs all the squares
var squares = document.querySelectorAll('td');

//  clear all the squares
function clearBoard() {
for( var i = 0; i < squares.length; i ++) {
     squares[i].textContent = '';
   }
   startBtn.textContent = 'Restart';
}
startBtn.addEventListener('click', clearBoard);

// check the square marker
function squareMarker() {
  if(this.textContent === ''){
    this.textContent = 'X';
  } else if(this.textContent === 'X') {
    this.textContent = 'O';
  } else {
    this.textContent = '';
  }
}
// for loop to add event listeners to all the squares
for (var i =0; i<squares.length; i++){
  squares[i].addEventListener('click', squareMarker);
}
