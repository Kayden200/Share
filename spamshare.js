function openFacebook() {
    window.open("https://m.facebook.com/login.php", "_blank");
}

function startSpamShare() {
    let postLink = document.getElementById("postLink").value;
    let shareCount = parseInt(document.getElementById("shareCount").value);

    if (!postLink || isNaN(shareCount) || shareCount < 1) {
        alert("Please enter a valid Facebook post link and share count.");
        return;
    }

    let i = 0;
    function sharePost() {
        if (i < shareCount) {
            let shareUrl = `https://m.facebook.com/sharer.php?u=${encodeURIComponent(postLink)}`;
            window.open(shareUrl, "_blank");
            i++;
            setTimeout(sharePost, 3000); // 3-second delay between shares
        } else {
            alert(`✅ Successfully shared ${shareCount} times!`);
        }
    }

    sharePost();
}
