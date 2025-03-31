const myHeading = document.querySelector('h1');
myHeading.textContent = 'Hello, World!';

let value = 10;

if ( value > 5 ){
    alert('Value is greater than 5');
} else {
    alert('Value is less than or equal to 5');
}

for (let i = 0; i < 5; i++) {
    console.log(i);
}

function fullName(firstName, lastName) {
    return firstName + ' ' + lastName;
}

console.log( fullName('Andrew', 'Solis') );

const input = document.getElementById('myInput');

// Global scope
let globalVar = 'I am a global variable';

input.addEventListener('keypress', (event) =>
{
    console.log(event.key)
    // Local scope within EventListener function
    let outerVar = 'I am an outer variable';

    const innerFunction = () => {
        // Local scope within innerFunction
        let innerVar = 'I am an inner variable';

        console.log(globalVar); // Accessible
        console.log(outerVar);  // Accessible
        console.log(innerVar);  // Accessible
    };

    innerFunction();
    console.log(globalVar); // Accessible
    console.log(outerVar);  // Accessible
    // console.log(innerVar); // Not accessible, would cause an error

});

console.log(globalVar); // Accessible
// console.log(outerVar); // Not accessible, would cause an error
// console.log(innerVar); // Not accessible, would cause an error




// Select the first paragraph element
const firstLink = document.querySelector('.nav-link');
console.log(firstLink.textContent); // Output: Home

// Select all paragraph elements
const allLinks = document.querySelectorAll('.nav-link');
allLinks.forEach(paragraph => {
    console.log(paragraph.textContent);
});