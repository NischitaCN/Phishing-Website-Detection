
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var url = tabs[0].url;
    document.getElementById('url').textContent = url;
    //to handle the phishing detection
    document.getElementById('check').addEventListener('click', function() {
      let counter = localStorage.getItem('counter') ? Number(localStorage.getItem('counter')) : Number(0);
      var markup = "url="+url+"&html="+document.documentElement.innerHTML;
      var xhr=new XMLHttpRequest();
      //xhr.open("POST","http://127.0.0.1:5000",false);
      xhr.open("POST","http://ec2-3-25-106-97.ap-southeast-2.compute.amazonaws.com:8080/",false);
      xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xhr.send(markup);
      var response = xhr.responseText.trim();
      var resultElement = document.getElementById('result');
      resultElement.textContent = response;
      if (response === "PHISHING") {
        counter = Number(counter) + 1;
        localStorage.setItem('counter', counter);
        resultElement.style.color = 'red';
      } else {
        resultElement.style.color = 'green';
      }
    });
    //to toggle the print of total count
    document.getElementById('printReport').addEventListener('click', function() {
      let counter = localStorage.getItem('counter') ? Number(localStorage.getItem('counter')) : Number(0);
      var phishElement = document.getElementById('report');
      if (phishElement.innerHTML === "") {
        phishElement.innerHTML = "Phishing detected <span style='color: red;   font-weight: bold;'>"+Number(counter)+"</span> times in Total"
      } else {
        phishElement.innerHTML = "";
      }
    });
  });
  