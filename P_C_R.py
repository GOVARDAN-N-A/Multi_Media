class MediaServer:
    def __init__(self):
        self.content_popularity = {}  # Dictionary to store content popularity

    def request_content(self, video_title):
        # Simulate a user request for content retrieval
        # In a real scenario, you would log this request and update content popularity accordingly
        if video_title not in self.content_popularity:
            self.content_popularity[video_title] = 1
        else:
            self.content_popularity[video_title] += 1

    def get_popular_content(self, num_items=5):
        # Get the most popular content based on request count
        sorted_content = sorted(self.content_popularity.items(), key=lambda x: x[1], reverse=True)
        return sorted_content[:num_items]

# Create a media server instance
media_server = MediaServer()

# Simulate content requests (videos)
media_server.request_content("Entertainment News: Celebrity Interviews")
media_server.request_content("Coding Challenge: Algorithmic Puzzles")
media_server.request_content("Movie Night: Classic Films Marathon")
media_server.request_content("Web Development Tutorial: Building a Blog")
media_server.request_content("Gaming Session: Online Multiplayer Adventure")
media_server.request_content("Comedy Show: Stand-up Comedy Special")
media_server.request_content("Coding Bootcamp: Python Crash Course")

# Get the top 3 popular videos
popular_content = media_server.get_popular_content(3)

# Print the popular videos
for video_title, popularity in popular_content:
    print(f"Video: {video_title}, Popularity: {popularity}")
