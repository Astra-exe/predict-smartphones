async function predictPrice() {
    const data = {
        RAM: parseFloat(document.getElementById('ram').value),
        age_years: parseFloat(document.getElementById('age').value),
        Battery_Capacity: parseFloat(document.getElementById('battery').value),
        Condition: document.getElementById('condition').value,
        Launched_Price_USA: parseFloat(document.getElementById('price').value)
    };

    try {
        const response = await fetch('http://localhost:3000/predict', {  // Cambiar puerto
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        const resultDiv = document.getElementById('result');
        
        resultDiv.innerHTML = `🤑 Un buen precio para tu refabricado sería: $${result.predicted_price} USD 🤑`;
        resultDiv.style.display = 'block';
        
    } catch (error) {
        alert('Error making prediction: ' + error.message);
    }
}