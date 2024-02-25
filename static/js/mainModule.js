
import { GoogleGenerativeAI } from "@google/generative-ai";

const API_KEY = "AIzaSyCrA_PpXKgO9vWZtuJSoK20KSTJNqR_9x8"; 
const genAI = new GoogleGenerativeAI(API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-pro" });

export { model };