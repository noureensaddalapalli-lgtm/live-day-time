
async function updateClock() {
    const status = document.getElementById("status");

    try {
        const response = await fetch("/api/time");

        if (!response.ok) {
            throw new Error("Could not get the time");
        }

        const data = await response.json();

        document.getElementById("day").textContent = data.day;
        document.getElementById("date").textContent = data.date;
        document.getElementById("time").textContent = data.time;

        status.textContent = "Connected to Python backend";
    } catch (error) {
        status.textContent = "Backend connection failed";
        console.error(error);
    }
}

updateClock();
setInterval(updateClock, 1000);
