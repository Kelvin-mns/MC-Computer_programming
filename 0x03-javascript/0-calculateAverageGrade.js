
function calculateAverageGrade(array) {
    var sum = 0;

    for (let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return sum / array.length
}
console.log("The average is: ", calculateAverageGrade([65, 80, 78, 82, 99]))