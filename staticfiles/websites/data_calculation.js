
function calculateFormerDuration() {
    console.log("calculateFormerDuration triggered");
    const startDate = document.getElementById("formerJob_start").value;
    const endDate = document.getElementById("formerJob_end").value;



    if (startDate && endDate) {
        const start = new Date(startDate);
        const end = new Date(endDate);

        let years = end.getFullYear() - start.getFullYear();
        let months = end.getMonth() - start.getMonth();

        if (months < 0) {
            years--;
            months += 12;
        }

        document.getElementById("duration").innerText = `${years} 年 ${months} 月`;
        document.getElementById('formerJob_totalTime').value = `${years} 年 ${months} 月`;

    }
}

function calculateFormerDuration() {
    const currentstartDate = document.getElementById("currentJob_start").value;
    const currentendDate = document.getElementById("currentJob_end").value;

    if (currentstartDate && currentendDate) {
        const currentstart = new Date(currentstartDate)
        const currentend = new Date(currentendDate)

        let currentyears = currentend.getFullYear() - currentstart.getFullYear();
        let currentmonths = currentend.getMonth() - currentstart.getMonth();

        if (currentmonths < 0) {
            currentyears--;
            currentmonths += 12;
        }
        document.getElementById("current_duration").innerText = `${currentyears} 年 ${currentmonths} 月`;
        document.getElementById('currentJob_totalTime').value = `${currentyears} 年 ${currentmonths} 月`;
    }

}


