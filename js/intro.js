// Variable
var a = 10;
console.log(a);

// uses variable
// var a = 10;
// let a = 10;
// const a = 10;

// var is a global variable
{
  var a = 10;
}
console.log(a);

// let is a private variable
{
  let a = 10;
  console.log(a);
}

// const is a constant variable
const a = 10;
a = 20;
console.log(a);
