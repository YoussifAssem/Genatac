// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCmuZGl5AWSah3INjLhA7fpZhXXMMtT1wk",
  authDomain: "paternitytest-7cb8b.firebaseapp.com",
  databaseURL: "https://paternitytest-7cb8b-default-rtdb.firebaseio.com",
  projectId: "paternitytest-7cb8b",
  storageBucket: "paternitytest-7cb8b.appspot.com",
  messagingSenderId: "86992490246",
  appId: "1:86992490246:web:4655ac1c84ecc003d1d887",
  measurementId: "G-70MRD19X3S"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);