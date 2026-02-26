"""
MkDocs Macros Plugin - Custom Macros for S3 School Lectures
"""


def define_env(env):
    """
    This is the hook for defining macros, filters, and variables.
    """

    @env.macro
    def pdf_iframe(url, height="600px"):
        """
        Embed a PDF with an iframe, fullscreen link, and download link.

        Args:
            url: The URL of the PDF file
            height: Height of the iframe (default: 600px)

        Usage:
            {{ pdf_iframe("https://example.com/slides.pdf") }}
            {{ pdf_iframe("https://example.com/slides.pdf", height="800px") }}
        """
        return f"""
<iframe src="{url}#view=FitH&toolbar=1&navpanes=0" 
        width="100%" 
        height="{height}" 
        allowfullscreen>
</iframe>

<a href="{url}" target="_blank">Open in Fullscreen Mode</a>

"""

    @env.macro
    def youtube_iframe(video_id, max_width="800px"):
        """
        Embed a YouTube video with an iframe that maintains 16:9 aspect ratio.

        Args:
            video_id: The YouTube video ID (the part after ?v= in the URL)
            max_width: Maximum width of the video container (default: 800px)

        Usage:
            {{ youtube_iframe("dQw4w9WgXcQ") }}
            {{ youtube_iframe("dQw4w9WgXcQ", max_width="1000px") }}
        """
        return f"""
<div style="max-width: {max_width}; margin: 0 auto;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
                src="https://www.youtube.com/embed/{video_id}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
        </iframe>
    </div>
</div>

"""
