async function startSpamShare() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let postLink = document.getElementById("postLink").value;
    let shareCount = document.getElementById("shareCount").value;

    if (!email || !password || !postLink || isNaN(shareCount) || shareCount < 1) {
        alert("Please fill all fields correctly.");
        return;
    }

    let requestData = {
        email: email,
        password: password,
        post_link: postLink,
        share_count: parseInt(shareCount)
    };

    try {
        let response = await fetch('/share', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        });

        let result = await response.json();
        alert(result.success || result.error);
    } catch (error) {
        alert("Server error. Please try again.");
    }
}
