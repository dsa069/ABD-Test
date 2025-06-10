document.addEventListener('DOMContentLoaded', function() {
    // Only execute on quiz page
    const questionContainer = document.getElementById('question-container');
    if (!questionContainer) return;

    const questionText = document.getElementById('question-text');
    const optionsContainer = document.getElementById('options-container');
    const feedbackContainer = document.getElementById('feedback-container');
    const feedbackText = document.getElementById('feedback-text');
    const nextBtn = document.getElementById('next-btn');
    const submitBtn = document.getElementById('submit-btn');
    const currentQuestionElement = document.getElementById('current-question');
    const correctAnswersElement = document.getElementById('correct-answers');
    const incorrectAnswersElement = document.getElementById('incorrect-answers');

    let selectedOption = null;
    let isMultipleChoice = false;
    let selectedOptions = [];
    
    // Load the first question
    loadQuestion();

    // Add event listeners
    nextBtn.addEventListener('click', loadQuestion);
    submitBtn.addEventListener('click', submitMultipleAnswers);

    // Load question function
    function loadQuestion() {
        // Hide feedback, next button and submit button
        feedbackContainer.style.display = 'none';
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'none';
        
        // Clear options and reset selections
        optionsContainer.innerHTML = '';
        selectedOption = null;
        selectedOptions = [];
        
        // Fetch the next question
        fetch('/get_question')
            .then(response => response.json())
            .then(data => {
                if (data.completed) {
                    // Quiz is completed, redirect to results
                    window.location.href = '/results';
                    return;
                }
                
                // Display the question
                questionText.textContent = data.question;
                
                // Store if this is a multiple choice question
                isMultipleChoice = data.isMultiple;
                
                // Show appropriate heading for question type
                if (isMultipleChoice) {
                    const multipleChoiceIndicator = document.createElement('p');
                    multipleChoiceIndicator.className = 'multiple-choice-indicator';
                    multipleChoiceIndicator.textContent = '(Selección múltiple - Selecciona todas las respuestas correctas)';
                    questionText.appendChild(multipleChoiceIndicator);
                    
                    // Show submit button for multiple choice
                    submitBtn.style.display = 'inline-block';
                }
                
                // Create and display the options
                data.options.forEach((option, index) => {
                    if (isMultipleChoice) {
                        // Create checkbox for multiple choice
                        const optionDiv = document.createElement('div');
                        optionDiv.className = 'option-checkbox';
                        
                        const checkbox = document.createElement('input');
                        checkbox.type = 'checkbox';
                        checkbox.id = 'option-' + index;
                        checkbox.value = index;
                        
                        const label = document.createElement('label');
                        label.htmlFor = 'option-' + index;
                        label.textContent = option;
                        
                        // Add event listeners for checkboxes
                        checkbox.addEventListener('change', function() {
                            if (this.checked) {
                                selectedOptions.push(parseInt(this.value));
                            } else {
                                const idx = selectedOptions.indexOf(parseInt(this.value));
                                if (idx > -1) selectedOptions.splice(idx, 1);
                            }
                        });
                        
                        optionDiv.appendChild(checkbox);
                        optionDiv.appendChild(label);
                        optionsContainer.appendChild(optionDiv);
                    } else {
                        // Create button for single choice
                        const optionBtn = document.createElement('button');
                        optionBtn.className = 'option-btn';
                        optionBtn.textContent = option;
                        optionBtn.dataset.index = index;
                        
                        optionBtn.addEventListener('click', function() {
                            if (selectedOption !== null) return; // Prevent multiple selections
                            
                            selectedOption = parseInt(index);
                            checkAnswer(selectedOption);
                        });
                        
                        optionsContainer.appendChild(optionBtn);
                    }
                });
            })
            .catch(error => {
                console.error('Error loading question:', error);
                questionText.textContent = 'Error cargando pregunta. Por favor, inténtalo de nuevo.';
            });
    }

    // Submit multiple answers
    function submitMultipleAnswers() {
        if (selectedOptions.length === 0) {
            alert('Debes seleccionar al menos una respuesta');
            return;
        }
        
        checkAnswer(selectedOptions);
    }

    // Check the answer
    function checkAnswer(selectedAnswer) {
        fetch('/check_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ selected: selectedAnswer })
        })
        .then(response => response.json())
        .then(data => {
            // Show the feedback
            feedbackContainer.style.display = 'block';
            
            if (data.correct) {
                feedbackText.textContent = '¡Correcto!';
                feedbackContainer.style.backgroundColor = '#d4edda';
                feedbackContainer.style.color = '#155724';
                
                // Update correct answers counter
                correctAnswersElement.textContent = parseInt(correctAnswersElement.textContent) + 1;
            } else {
                // Different feedback for multiple vs single choice
                if (isMultipleChoice) {
                    feedbackText.textContent = '¡Incorrecto! Las respuestas correctas eran: ';
                    const correctOptionIndices = data.correctOption;
                    
                    let correctLabels = [];
                    correctOptionIndices.forEach(index => {
                        // Get the labels of all correct options
                        const label = document.querySelector(`label[for="option-${index}"]`).textContent;
                        correctLabels.push(label);
                    });
                    
                    feedbackText.textContent += correctLabels.join(', ');
                } else {
                    feedbackText.textContent = '¡Incorrecto! La respuesta correcta era: ' + 
                        optionsContainer.children[data.correctOption].textContent;
                }
                
                feedbackContainer.style.backgroundColor = '#f8d7da';
                feedbackContainer.style.color = '#721c24';
                
                // Update incorrect answers counter
                if (incorrectAnswersElement) {
                    incorrectAnswersElement.textContent = parseInt(incorrectAnswersElement.textContent || 0) + 1;
                }
            }
            
            // Mark options as correct/incorrect
            if (isMultipleChoice) {
                // For multiple choice questions
                Array.from(optionsContainer.children).forEach((optionDiv, index) => {
                    const checkbox = optionDiv.querySelector('input[type="checkbox"]');
                    checkbox.disabled = true;
                    
                    if (data.correctOption.includes(parseInt(checkbox.value))) {
                        optionDiv.classList.add('option-correct');
                    } else if (selectedOptions.includes(parseInt(checkbox.value))) {
                        optionDiv.classList.add('option-incorrect');
                    }
                });
                
                // Hide submit button
                submitBtn.style.display = 'none';
            } else {
                // For single choice questions
                Array.from(optionsContainer.children).forEach((option, index) => {
                    option.disabled = true;
                    
                    if (index === data.correctOption) {
                        option.classList.add('option-correct');
                    } else if (index === selectedAnswer && !data.correct) {
                        option.classList.add('option-incorrect');
                    }
                });
            }
            
            // Show next button if there are more questions
            if (data.nextQuestion) {
                nextBtn.style.display = 'inline-block';
                
                // Update question counter
                currentQuestionElement.textContent = parseInt(currentQuestionElement.textContent) + 1;
                
                // Update progress bar
                const total = parseInt(document.getElementById('total-questions').textContent);
                const current = parseInt(currentQuestionElement.textContent);
                document.querySelector('.progress-fill').style.width = `${(current / total) * 100}%`;
            } else {
                // Quiz is complete, show results button
                nextBtn.textContent = 'Ver resultados';
                nextBtn.style.display = 'inline-block';
            }
        })
        .catch(error => {
            console.error('Error checking answer:', error);
            feedbackContainer.style.display = 'block';
            feedbackText.textContent = 'Error al verificar respuesta. Por favor, inténtalo de nuevo.';
        });
    }
});