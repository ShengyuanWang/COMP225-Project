// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyADMm4loBketoIcywbMW9HvcaLcjrM4Hqk",
    authDomain: "comp225-810dc.firebaseapp.com",
    projectId: "comp225-810dc",
    storageBucket: "comp225-810dc.appspot.com",
    messagingSenderId: "1015003809592",
    appId: "1:1015003809592:web:58d9dff83c57b41564a3cd",
    measurementId: "G-LWT5X222PT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

import { getStorage } from 'firebase/storage';
const storage = getStorage(app);

export {storage}
