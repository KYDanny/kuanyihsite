//為了讓checkbox7個1列
const container = document.getElementById("checkbox-container");
const checkboxes = document.querySelectorAll("input[type='checkbox']");

let currentRow = document.createElement("div");
currentRow.classList.add("row");
checkboxes.forEach((checkbox, index) => {
    if (index > 0 && index % 7 === 0) {
    container.appendChild(currentRow);
        currentRow = document.createElement("div");
        currentRow.classList.add("row");
    }
    })
    container.appendChild(currentRow);