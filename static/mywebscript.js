let runAddition = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    let result = num1 + num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runSubtraction = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    let result = num1 - num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runMultiplication = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);

    let result = num1 * num2;
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

let runDivision = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    var result = 0;
    if (num2 ==0)
    {
        alert("canot dividig by zero");
         result = "canot dividig by zero";
    }
    else
    {
         result = num1 / num2;
    }
    document.getElementById("system_response").innerHTML = "Result: " + result;
};