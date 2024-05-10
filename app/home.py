from st_pages import Page, show_pages, add_page_title
from views import home, about, analysis, options, configuration
import utils 

# Optional -- adds the title and icon to the current page
add_page_title(
    page_title="Welcome to new platform",
    page_icon="👋"
)


# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("pages/1_📈_Plotting_Demo.py", "Plot", "📈"),
        Page("pages/2_🌍_Mapping_Demo.py", "Map", "🌍"),
        Page("pages/3_📊_DataFrame_Demo.py", "DataFrame", "📊"),
        Page("pages/example.py", "Example", "🧪"),
        Page("pages/table.py", "Grid", "🌐"),
        Page("pages/table2.py", "Results", "🎯")
    ]
)

utils.inject_custom_css()
utils.navbar_component()

def navigation():
    route = utils.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "about":
        about.load_view()
    elif route == "analysis":
        analysis.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()
