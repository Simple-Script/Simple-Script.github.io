<!DOCTYPE html><html lang=en><head><meta charset=UTF-8><meta name=viewport content="width=device-width,initial-scale=1"><title>SimpleScript</title><body><div id=output></div><script>fetch('https://raw.githubusercontent.com/Kellarosaa/ss-workload/refs/heads/main/index.ss').then(response=>response.text()).then(data=>{const regex=/text\((.*?)\)/g;let matches;let output='';while((matches=regex.exec(data))!==null){output+=matches[1]+'<br>';}document.getElementById('output').innerHTML=output;}).catch(error=>console.error('Error fetching the file:',error));</script><style>.redirect-link{color:#00f;text-decoration:underline}</style><div id=content></div><script>async function fetchGitHubFile(){const response=await fetch('https://raw.githubusercontent.com/Kellarosaa/ss-workload/refs/heads/main/index.ss');const text=await response.text();const regex=/https:\/\/[^\s]+/g;const matches=text.match(regex);const contentDiv=document.getElementById('content');if(matches){matches.forEach(url=>{const link=document.createElement('a');link.href=url;link.className='redirect-link';link.target='_self';link.innerText=url;contentDiv.appendChild(link);contentDiv.appendChild(document.createElement('br'));});}else{contentDiv.innerText='No links found.';}}fetchGitHubFile();</script>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <script>
        const url = 'https://raw.githubusercontent.com/Kellarosaa/ss-workload/refs/heads/main/index.ss';
        
        fetch(url)
            .then(response => response.text())
            .then(data => {
                const regex = /button\(([^)]+)\)/g;
                let match;
                while ((match = regex.exec(data)) !== null) {
                    const [fullMatch, link] = match;
                    const buttonText = link.split('-')[0];
                    const buttonLink = link.split('-')[1];
                    const button = document.createElement('button');
                    button.innerText = buttonText;
                    button.onclick = () => window.open(`https://${buttonLink}`, '_self');
                    document.body.appendChild(button);
                }
            })
            .catch(error => console.error('Error fetching the file:', error));
    </script>
</body>
</html>