document.getElementById('submit-button').addEventListener('click', async () => {
  const userInput = document.getElementById('user_input').value;
  const outputElement = document.getElementById('output');

  try {
    const response = await fetch('https://ai-chrome-extension.onrender.com/api/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: userInput }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.statusText}`);
    }

    const result = await response.json();
    outputElement.innerText = result.answer;
  } catch (error) {
    console.error('There has been a problem with your fetch operation:', error);
    outputElement.innerText = 'An error occurred: ' + error.message;
  }
});
