"use strict";


function copyToClipboard(id) {
    
    var from = document.getElementById(id);
    var range = document.createRange();
    window.getSelection().removeAllRanges();
    range.selectNodeContents(from);
    window.getSelection().addRange(range);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
}

function encryptButtonClicked() {
    
    let encryptionForm = document.getElementById("encryption_form");
    
    if (encryptionForm.style.display != "") return;
    
    let encryptBtn = document.getElementById("encrypt_button");
    encryptBtn.style.border = "3px #74d14c solid";
    
    let decryptBtn = document.getElementById("decrypt_button");
    decryptBtn.style.border = "none";
    
    let keysGeneratorBtn = document.getElementById("keys_generation_button");
    keysGeneratorBtn.style.border = "none";
    
    encryptionForm.style.display = "inline-block";
    let decryptionForm = document.getElementById("decryption_form");
    decryptionForm.style.display = "";
    let keysGenerator = document.getElementById("keys_generator");
    keysGenerator.style.display = "";
    let processedMessage = document.getElementById("processed_text");
    if (processedMessage) processedMessage.style.display = "none";

  }

function decryptButtonClicked() {
    
    let decryptionForm = document.getElementById("decryption_form");
    
    if (decryptionForm.style.display != "") return;
    
    let decryptBtn = document.getElementById("decrypt_button");
    decryptBtn.style.border = "3px #74d14c solid";
    
    let encryptBtn = document.getElementById("encrypt_button");
    encryptBtn.style.border = "none";
    
    let keysGeneratorBtn = document.getElementById("keys_generation_button");
    keysGeneratorBtn.style.border = "none";
    
    decryptionForm.style.display = "inline-block";
    let encryptionForm = document.getElementById("encryption_form");
    encryptionForm.style.display = "";
    let keysGenerator = document.getElementById("keys_generator");
    keysGenerator.style.display = "";
    let processedMessage = document.getElementById("processed_text");
    if (processedMessage) processedMessage.style.display = "none";    
  }

function keysGenerationButtonClicked() {
    
    let keysGenerator = document.getElementById("keys_generator");
    
    if (keysGenerator.style.display != "") return;
    
    let keysGeneratorBtn = document.getElementById("keys_generation_button");
    keysGeneratorBtn.style.border = "3px #74d14c solid";
    
    let decryptBtn = document.getElementById("decrypt_button");
    decryptBtn.style.border = "none";
    
    let encryptBtn = document.getElementById("encrypt_button");
    encryptBtn.style.border = "none";
    
    keysGenerator.style.display = "inline-block";
    let encryptionForm = document.getElementById("encryption_form");
    encryptionForm.style.display = "";
    let decryptionForm = document.getElementById("decryption_form");
    decryptionForm.style.display = "";
    let processedMessage = document.getElementById("processed_text");
    if (processedMessage) processedMessage.style.display = "none";    
  }
