// have a nice day if you are reading this 😊

window.onload = () => {    
    updatePage()
    setInterval(updatePage, 15000)
}

function redirect(page) {
    window.open(page, "_blank")
}

async function handleSubmit() {
    let formValue = document.getElementById("message-text").value
    let closeButton = document.getElementById("closeButton")

    await fetch("/api/update", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({newCode: formValue})
      })
    
    let toast = document.getElementById("liveToast")
    toast = new bootstrap.Toast(toast)

    closeButton.click()
    toast.show()

}

async function updatePage() {
    let r = await fetch("/api/code", {
        headers: {"Content-Type": "application/json"},
    })
    r = await r.json()

    let userCode = document.getElementById("message-text").value

    if (!userCode) document.getElementById("message-text").value = r.code

    document.getElementById("site").innerHTML = r.code

}