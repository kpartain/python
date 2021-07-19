async function getHoroscope() {
    var apiRequest = await fetch('https://aztro.sameerkumar.website/?sign=pisces&day=today', {method: 'POST'}
    );
    var apiResponse = await apiRequest.json();
    document.getElementById("todays-reading").innerText = apiResponse.description;
    document.getElementById("lucky-number").innerText = apiResponse.lucky_number;
    document.getElementById("lucky-time").innerText = apiResponse.lucky_time;
    document.getElementById("todays-mood").innerText = apiResponse.mood;
  }
  
  getHoroscope();