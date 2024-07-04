const apiUrl = "http://localhost:8000"; // Thay đổi thành URL thực tế của API của bạn

async function generateText() {
  const inputText = document.getElementById('inputText').value;

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: inputText })

    });

    if (!response.ok) {

      throw new Error('Không thể tạo văn bản. Vui lòng thử lại sau.');

    }

    const data = await response.json();
    displayResult(data.result);
  } catch (error) {
    console.error('Đã xảy ra lỗi:', error);
    alert('Đã xảy ra lỗi. Vui lòng thử lại sau.');
  }
}

function displayResult(result) {
  const outputDiv = document.getElementById('output');
  outputDiv.innerHTML = `<p>${result}</p>`;
}
