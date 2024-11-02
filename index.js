document.getElementById('musicMatchForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
  
    // Collect the five musician inputs
    const musicians = [
      document.getElementsByName('musician1')[0].value,
      document.getElementsByName('musician2')[0].value,
      document.getElementsByName('musician3')[0].value,
      document.getElementsByName('musician4')[0].value,
      document.getElementsByName('musician5')[0].value
    ];
  
    // Now you can use the 'musicians' array for your matching algorithm
    console.log("User info:", { name, age, gender, musicians });
    // Call your matching function here
  });
  