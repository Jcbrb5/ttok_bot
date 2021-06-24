const TikTokScraper = require('tiktok-scraper');

// User feed by username
(async () => {
    try {
        const posts = await TikTokScraper.user('areyouhapppy', {
            number: 0,
            sessionList: ['sid_tt=58ba9e34431774703d3c34e60d584475;'],
            filepath: "/Users/jacobrubin/Documents/Northeastern 3rd Year/Artificial Intelligence/tiktok_ml_project",
            fileName: "out",
            filetype: "csv"
        });
        console.log(posts);
    } catch (error) {
        console.log(error);
    }
})();