import { model } from "/static/js/mainModule.js";
const chatInput = document.querySelector("#chat-input");
const sendButton = document.querySelector("#send-btn");
const chatContainer = document.querySelector(".chat-container");
const getChatResponse = async () => { 
        const userText = chatInput.value.trim(); 
        const pEle = document.createElement("p"); 

        try { 
            const result = await model.generateContent(userText); 
            const response = await result.response.text(); 
            pEle.textContent = response.trim(); 
        } catch (error) { 
                pEle.classList.add("error"); 
                pEle.textContent = "Oops! Something went wrong while retrieving the response. Please try again.";
        } 
        chatContainer.appendChild(pEle); 
    } 
chatInput.addEventListener("keydown", (e) => { 
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) 
        { 
            e.preventDefault(); 
            getChatResponse(); 
        } 
    }); 
const handleAPI = () => { 
    const userText = chatInput.value.trim(); 
    if (!userText) return; 
    chatInput.value = ""; 
    const html = ` <div class="chat-content">
                     <div class="chat-body-inner">  
                        <span class="icon"><i class='bx bxs-user'></i></span> 
                        <p>${userText}</p> 
                    </div> 
                </div>`; 
chatContainer.innerHTML += html; 
getChatResponse(); 
} 
sendButton.addEventListener("click", handleAPI);