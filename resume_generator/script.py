import pdfkit
from jinja2 import Environment, FileSystemLoader
from profiles.models import Profile

def generate_resume(profile_id):
    # Load profile data
    profile = Profile.objects.get(id=profile_id)
    
    # Select template based on location
    template_map = {
        "US/Canada": "resume_us.html",
        "UK": "resume_uk.html",
        # Add paths for other templates...
    }
    template_path = template_map.get(profile.location, "resume_us.html")

    # Configure Jinja2 template environment
    env = Environment(loader=FileSystemLoader('/path/to/your/templates'))
    template = env.get_template(template_path)

    # Render HTML
    html_content = template.render(profile=profile)

    # Convert to PDF
    output_path = f"/path/to/save/{profile.name}_resume.pdf"
    pdfkit.from_string(html_content, output_path)

    print("Resume generated:", output_path)

if __name__ == "__main__":
    import sys
    profile_id = sys.argv[1]
    generate_resume(profile_id)
