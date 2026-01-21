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
