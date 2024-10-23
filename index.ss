sigma(This language is very small and is mainly used in python. I have ideas to make it a markdown language and improve the syntax.)
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .bar {
            display: flex;
            height: 30px;
            margin: 10px 0;
        }
        .smdl {
            background-color: purple;
        }
        .html {
            background-color: red;
        }
        .ss {
            background-color: blue;
        }
    </style>
</head>
<body>

<div id="visualization"></div>

<script>
    const urls = [
        "https://raw.githubusercontent.com/Kellarosaa/ss-workload/refs/heads/main/index.ss",
        "https://raw.githubusercontent.com/Kellarosaa/ss-workload/refs/heads/main/index.html",
        "https://raw.githubusercontent.com/Kellarosaa/ss-workload/refs/heads/main/README.smdl"
    ];

    async function fetchData(url) {
        const response = await fetch(url);
        return await response.text();
    }

    async function visualize() {
        const results = await Promise.all(urls.map(fetchData));
        const lengths = results.map(text => text.length);
        const totalLength = lengths.reduce((a, b) => a + b, 0);
        
        const visualization = document.getElementById('visualization');
        const fileTypes = ['.ss', '.html', '.smdl'];
        const colors = ['blue', 'pink', 'purple'];

        lengths.forEach((length, index) => {
            const percentage = (length / totalLength) * 100;
            const bar = document.createElement('div');
            bar.className = 'bar ' + fileTypes[index].slice(1);
            bar.style.width = percentage + '%';
            bar.textContent = `${fileTypes[index]}: ${percentage.toFixed(2)}%`;
            visualization.appendChild(bar);
        });
    }

    visualize();
</script>

</body>
</html>
