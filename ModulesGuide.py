import os
import logging
import qt
import slicer
import slicer.ScriptedLoadableModule as scripted



class ModulesGuide(scripted.ScriptedLoadableModule):
    def __init__(self, parent):
        scripted.ScriptedLoadableModule.__init__(self, parent)
        self.parent = parent
        self.parent.title = "Modules Guide"
        self.parent.categories = ["Utilities"]
        self.parent.icon = qt.QIcon(os.path.join(os.path.dirname(__file__), "ModulesGuide.jpg"))
        self.parent.dependencies = []
        self.parent.contributors = ["Mohamed Alalli Bilal (Mauritania)"]
        self.parent.helpText = """
        <b>3D Slicer Modules Guide Learning Assistant</b><br>
        This interactive assistant was built to simplify the learning journey for newcomers to the 3D Slicer platform. 
        Whether you're a medical student, researcher, or developer just starting with Slicer, 
        this tool provides easy access to essential knowledge about each module.<br>
        Select a module from the list to read the description.<br><br>
        """
        self.parent.acknowledgementText = "Created as a training project using Python only."

class ModulesGuideWidget(scripted.ScriptedLoadableModuleWidget):
    def setup(self):
        self.layout = self.parent.layout()

        mainLayout = qt.QVBoxLayout()
        mainLayout.setSpacing(10)

        title = qt.QLabel("🔍 3D Slicer Modules Guide Learning Assistant")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E86C1; margin: 10px 0px;")
        mainLayout.addWidget(title)

        label = qt.QLabel("Select a module to view the description:")
        label.setStyleSheet("font-weight: bold; font-size: 14px;")
        mainLayout.addWidget(label)

        self.toolSelector = qt.QComboBox()
        self.help_data = help_data  # استخدم البيانات المدمجة

        for tool_name in self.help_data.keys():
            self.toolSelector.addItem(tool_name)

        self.toolSelector.currentIndexChanged.connect(self.showHelp)
        mainLayout.addWidget(self.toolSelector)

        self.textBox = qt.QTextBrowser()
        self.textBox.setStyleSheet("background-color: #1e1e1e; color: #ffffff; border: 1px solid #ccc; font-size: 14px; padding: 6px;")
        self.textBox.setMinimumHeight(120)
        mainLayout.addWidget(self.textBox)

        self.layout.addLayout(mainLayout)
        self.showHelp()

    def showHelp(self):
        tool_name = self.toolSelector.itemText(self.toolSelector.currentIndex)
        description = self.help_data.get(tool_name, "No help available for this tool.")
        self.textBox.setText(description)


help_data = {
    "Select a module ": "",
    "Data":
    """
    The Data module is a core utility in 3D Slicer that provides a hierarchical view of all data loaded into the application. It is essential for organizing, inspecting, and managing the datasets used in medical image analysis, surgical planning, and visualization.

    🔧 Main Features:

    * Subject Hierarchy Tree: Displays the structure of data, including patients, studies, series, volumes, models, segmentations, and markups. You can group and organize them logically.

    * Visibility Control: Quickly show or hide individual data elements using the eye icon next to each item.

    * Rename / Delete / Export: Right-click on any item to rename, delete, or export it. You can also re-parent items by dragging them in the tree.

    * Transform Management: Apply or remove transforms to/from data nodes, and visualize their effect.

    * Color and Display Settings: Customize how data is displayed using the display properties.

    * Metadata and Attributes: View or edit metadata like descriptions, DICOM tags, and custom attributes.

    🧠 Typical Use Cases:

    * Organizing loaded medical datasets (MRI, CT, Ultrasound, etc.)

    * Managing segmentations, fiducial points, and models

    * Applying registration or transformation to specific nodes

    * Cleaning or preparing data before processing or exporting

    """,

    "DICOM":
    """
    The DICOM module is the gateway for importing, browsing, and managing DICOM (Digital Imaging and Communications in Medicine) files in 3D Slicer. It enables users to interact with clinical imaging data in a standardized format used widely in hospitals and medical imaging systems.

    🔧 Main Features:

    * DICOM Browser: Shows a table of patients, studies, and series stored in Slicer's local DICOM database.

    * Import DICOM Files: Load DICOM images from local folders or directly from removable media (CD/DVD, USB, etc.).

    * Load into Slicer: Once imported, datasets can be loaded as volume nodes, segmentation nodes, etc., using the "Load" button.

    * DICOM Plugins: Uses specialized plugins to load complex data such as multi-frame MRIs, RTSTRUCT, SEG, or secondary capture images.

    * Export DICOM: You can export loaded and processed data (e.g., segmentations or label maps) back to DICOM format using Slicer’s DICOM export tools.

    * Query / Retrieve (DICOM Networking):

        * If configured, the module can connect to PACS systems over the network.

        * Supports DICOM Query/Retrieve (C-FIND, C-MOVE, C-GET) operations for fetching studies from external DICOM servers.

    🧠 Typical Use Cases:

    * Loading CT or MRI scans for diagnosis, research, or surgical planning.

    * Importing DICOM-RT data (e.g., radiation therapy contours).

    * Exporting processed data (e.g., 3D segmentation of tumors) as DICOM SEG for clinical use.

    * Fetching data from a PACS system directly into Slicer.

    """,

    "Markups":
    """
    The Markups module allows users to create, edit, and manage point-based annotations and geometric shapes within 3D Slicer. It is a powerful tool for placing landmarks, defining measurements, and guiding surgical planning or image analysis workflows.

    🔧 Main Features:

    * Fiducials (Points): Place anatomical landmarks, reference points, or points of interest in 2D and 3D views.

    * Lines & Curves: Draw straight lines or smooth curves (open or closed) between control points to measure lengths or guide segmentations.

    * Planes: Define a plane using 3 or more points—useful for orienting images or defining cutting/slicing planes.

    * Angles: Create angle measurements between three points (e.g., joint angles, lesion orientation).

    * ROI (Region of Interest): Create a 3D bounding box used for cropping volumes, focusing views, or controlling segment editor operations.

    * Measurements & Labels: Automatically calculates distances, angles, and other metrics. You can customize labels, colors, and visibility.

    * Editable Table View: All control points and measurements are shown in a table. You can rename, adjust coordinates, lock/unlock, or delete points directly from the table.

    * Interactive Placement: Use the mouse to click and place points in the 2D slice or 3D view, with real-time feedback.

    🧠 Typical Use Cases:

    * Placing anatomical landmarks for surgical navigation or comparison

    * Measuring tumor size, organ dimensions, or distances between structures

    * Defining cutting planes for volume rendering or segmentation

    * Annotating datasets for training AI models or clinical studies

    * Creating guiding curves for 3D modeling or prosthetic design

    """, 

    "Models": 
    """
    The Models module is designed to visualize, inspect, and manage 3D surface models within Slicer. These models typically represent anatomical structures, segmentations, or imported 3D objects (e.g., STL or OBJ files).

    🔧 Main Features:

    * View and Organize Models: Displays a list of all loaded model nodes (e.g., bones, organs, implants). You can toggle visibility, rename, group, and reassign models easily.

    * Display Settings:

        * Color & Opacity: Change the color and transparency of models.

        * Lighting and Shading: Adjust surface shading, specular lighting, and edge visibility.

        * Backface culling: Hide internal surfaces for better visibility of thin or hollow models.

        * Scalar coloring: Color the model based on scalar values like labels or intensity (e.g., functional data, temperature, etc.).

    * Model Hierarchies: Group multiple models into folders (subject hierarchy) for organized display and interaction.

    * Measurement Support: View surface area and volume of models if computed via other modules (like Segment Statistics).

    * Clip and Transform: Models can be clipped with ROI boxes or transformed using linear or non-linear transforms.

    📦 Model File Support:

    You can import or export 3D models in common formats:

        * Supported formats: .stl, .obj, .vtk, .vtp, .ply, etc.

        * Easily export segmentations to 3D models (e.g., tumor surface or bone reconstruction).

    🧠 Typical Use Cases:

    * Visualizing anatomical structures segmented from CT or MRI

    * Importing surgical implants, prosthetics, or 3D designs

    * Inspecting 3D models for research, education, or surgical simulation

    * Applying transformations or overlaying multiple anatomical surfaces

    * Preparing models for 3D printing

    """,

    "Scene Views":
    """
    The Scene Views module allows users to save and restore customized views of the 3D Slicer scene, including camera positions, visibility of elements, and window layouts. Think of it as a way to create “snapshots” of your session that you can return to later.

    🔧 Main Features:

    * Save Scene View:

        * Captures the current state of the application, including:

            * 3D/2D view orientations

            * Visibility of volumes, models, segmentations, and markups

            * Window layouts

            * Camera positions

        * Optionally add a screenshot and a description.

    * Restore Scene View:

        * Click on a saved view to instantly return to that visual state.

        * Helps when comparing different perspectives or presentation steps.

    * Manage Multiple Views:

        * Create as many views as needed.

        * Rename, delete, or reorder scene views using the module’s interface.

    * Visual Timeline for Tutorials:

        * Commonly used in education, presentations, or step-by-step demonstrations, where you guide users through a scene in stages.

    🧠 Typical Use Cases:

    * Creating teaching or demo materials with multiple viewpoints

    * Saving key steps during segmentation or surgical planning

    * Quickly switching between different visualizations of the same dataset

    * Preparing visual bookmarks for presentations or research documentation

    ⚠️ Limitations:

    * Scene views do not save the entire scene to disk—they are snapshots saved inside the currently loaded scene, and are lost if the scene is cleared or not saved.

    """,

    "Segmentations":
    """
    The Segmentations module is a powerful tool for managing segmented anatomical structures, lesions, or regions of interest. It allows users to create, edit, visualize, and export segmentations derived from medical images such as CT, MRI, or ultrasound scans.

    🔧 Main Features:

    * Create and Edit Segmentations:

        * Segmentations consist of one or more segments (e.g., liver, tumor, bone).

        * Each segment can be visualized in 2D slices or 3D renderings.

        * Edits are typically done using the Segment Editor module, but the Segmentations module provides an overview and tools for management.

    * Supported Representations:

        * Binary labelmaps (voxel-based)

        * Closed surfaces (3D mesh)

        * Fractional labelmaps, Contours, etc.

        * Automatically converts between representations as needed.

    * Visibility and Appearance:

        * Toggle visibility of individual segments.

        * Adjust segment color and opacity.

        * Show 2D and 3D outlines, filled areas, or both.

    * Import/Export Capabilities:

        * Convert segmentations to labelmaps or 3D models.

        * Import labelmaps, models, or other segmentation formats.

        * Export to formats like STL, OBJ, NRRD, or DICOM SEG.

    * Merge, Copy, Split:

        * Combine segmentations or split them into separate nodes.

        * Copy segments between segmentation nodes.

        * Apply transformations to segmentations.

    🧠 Typical Use Cases:

        * Manual or semi-automatic tumor/organ segmentation from imaging data.

        * Preparing data for 3D printing, surgical planning, or simulation.

        * Creating ground truth for AI model training.

        * Exporting results for clinical use in DICOM SEG format.

        * Visualizing multiple structures simultaneously in 3D.

    🔄 Integration with Other Modules:

    * Segment Editor: For advanced editing tools.

    * Models: For converting and viewing segmentation as surface models.

    * Volume Rendering: Combine with volume views for rich visualization.

    * DICOM: Export segmentations back into clinical PACS systems.

    """,

    "Segment Editor": 
    """
    The Segment Editor is the main tool in 3D Slicer for creating, modifying, and refining segmentations. It provides a set of powerful interactive tools (called effects) that allow users to label and isolate anatomical structures, lesions, or regions of interest in 2D and 3D.

    🔧 Main Features:

    * Interactive Editing Tools (Effects):
    The Segment Editor offers over 20 tools to manually or semi-automatically segment structures, including:

        * Paint: Freehand drawing in 2D slices.

        * Draw: Draw closed shapes (polygons).

        * Threshold: Select voxels based on intensity.

        * Grow from seeds: AI-based segmentation from labeled regions.

        * Scissors: Cut away parts of segments.

        * Level tracing: Follows edges with similar intensities.

        * Smoothing: Remove jagged edges from segmented regions.

        * Islands: Keep/remove connected components.

    * Undo/Redo: Full support for undoing or redoing operations per segment.

    * Multiple Segments Support:

        * Add as many segments as needed.

        * Switch between them easily for separate editing.

        * Choose different colors and names per segment.

    * Masking and Overlays:

        * Limit editing to a specific volume region or inside another segment.

        * Show/hide overlays for reference.

    * 3D Visualization:

        * Real-time 3D display of the segments.

        * Combine with volume rendering for advanced visual context.

    * Auto-conversion:

        * Handles automatic conversion between labelmaps and 3D surfaces.

        * Supports multiple internal representations like binary labelmaps and closed surfaces.

    🧠 Typical Use Cases:

    * Manually delineating organs, tumors, or vessels from CT/MRI.

    * Creating precise 3D printable models for planning or education.

    * Preparing annotated data for machine learning.

    * Visualizing structures in 3D for surgical guidance.

    * Cleaning up or refining automatic segmentation results.

    🔄 Integration with Other Modules:

    * Segmentations: Stores and manages the segmented structures.

    * Volumes: Provides the image data used for editing.

    * Models: Converts segments to surface models.

    * DICOM: Export segmentations as DICOM SEG for clinical use.

    """,

    "Welcome":
    """
    The Welcome module is the default home screen of 3D Slicer. It provides a quick starting point for users when they open the application. Its goal is to help new and returning users quickly access key resources and begin working efficiently.

    🧰 Main Features:

    * Recent Files:

        * Displays a list of recently opened scenes and data files.

        * Allows one-click loading of your recent work.

    * Quick Access Buttons:

        * Open DICOM browser

        * Load data from files

        * Load sample data

        * Restore a previously saved scene

    * Sample Data:

        * Provides downloadable demo datasets (CT, MRI, segmentations, etc.) for testing and learning.

        * Great for first-time users and training.

    * Resources and Help:

        * Links to documentation, community forum, tutorials, and extensions manager.

        * Ensures users have access to learning materials and support.

    * Extension Manager Access:

        * Shortcut to open the Extension Manager where users can browse and install add-ons.

    * Language and Appearance Settings (if configured):

        * May include quick access to UI preferences.

    🧠 Typical Use Cases:
    
        * Beginners launching Slicer for the first time and looking for where to start.

        * Quickly accessing sample data or recent projects.

        * Opening the DICOM browser without going through the menu.

        * Exploring learning resources and tutorials.
    """,

    "Transforms":
    """
    The Transforms module allows users to create, apply, and manage spatial transformations for aligning or repositioning images, models, markups, or any other objects in 3D space.

    It’s an essential module for registration, motion correction, coordinate alignment, and pose adjustments in medical imaging workflows.

    🔧 Main Features:

    * Types of Transforms:

        * Linear transforms (translations, rotations, scaling)

        * Non-linear transforms (warping, displacement fields)

        * Transforms can be manual or imported from registration modules or external sources.

    * Interactive Transform Editor:

        * Adjust translation and rotation interactively using sliders or numeric inputs.

        * View the transformation matrix in real time.

    * Apply/Remove Transform:

        * Use the Data module or the Transforms module to apply a transform to any node (e.g., volume, model, markup).

        * Applying a transform changes how the object appears in the scene but does not alter its actual voxel data (unless hardened).

    * Harden Transform:

        * Makes the transformation permanent by applying it to the data (resampling for images or modifying points for models).

    * Transform Hierarchies:

        * Transforms can be nested: child transforms inherit transformations from parents.

        * Useful for complex multi-object registration or motion sequences.

    * Visualization:

        * Visualize displacement fields or vector fields for non-linear transforms.

        * Combine with volume rendering or fiducials to assess transformation effects.

    🧠 Typical Use Cases:

    * Aligning CT/MRI images from different time points or modalities

    * Applying registration results to volumes, models, or segmentations

    * Simulating patient motion or adjusting surgical plans

    * Transforming 3D objects into a common coordinate system

    * Preparing data for export with aligned geometry

    🔄 Integration with Other Modules:

    * Registration modules (e.g., General Registration, BRAINS, Elastix): generate transforms.

    * Volumes, Models, Segmentations: can all be transformed and hardened.

    * Scene Views: stores current transform states for restoring later.
    """,

    "View Controllers":
    """
    The View Controllers module is the central dashboard for configuring every 2D slice view and the 3D view. It lets you fine-tune how images, models, and segmentations are displayed and interact across the different viewers.

    🔧 Main Controls & Options

    * Slice View Selectors :  Pick which volume (e.g., CT, MRI) appears in each slice viewer (Red, Yellow, Green, etc.).
    
    * Slice Visibility & Layout :  Toggle slice visibility, link/unlink cursors, and choose multi-pane layouts.
    
    * Slice Offset & Field of View :  Scroll through slices (mouse-wheel or slider) and jump to landmarks or fiducials.
    
    * Slice Orientation :  Switch between Axial, Sagittal, Coronal, or any oblique orientation (including Reformat mode).
    
    * Volume Rendering Sync :  Couple volume rendering settings to slice positions for synchronized exploration.
    
    * 3D Camera Controls :  Reset or center the 3D camera, adjust zoom, and set predefined viewpoints (e.g., Anterior, Left).
    
    * Linked/Independent :  Controls Link slice viewers so they move together, or work independently for comparison.
    
    * Slice Fade & Lightbox :   Blend two volumes in a slice (useful for pre-/post-contrast) and display lightbox grids.
    
    * Cross-hair & Ruler :  Show a cross-hair cursor across all views and display rulers with customizable units.

    🧠 Typical Use Cases

    * Side-by-Side Comparison: Display two modalities (e.g., CT vs. PET) in linked slice views for fusion analysis.

    * Surgical Planning: Lock slice viewers to specific planes through fiducials or reformat on-the-fly to match surgical angles.

    * Teaching & Demonstrations: Quickly switch layouts or viewpoints while explaining anatomy to students.

    * Quality Assurance: Scroll synchronously through time-series images to detect motion or artifacts.

    🔗 Related Modules

    * Data: Manages which volumes and models are available to assign to views.

    * Volume Rendering: Uses slice positions and camera settings for live 3D context.

    * Transforms: Alters how objects appear in all linked viewers.

    * Scene Views: Saves complete visual setups (including all view-controller states) for later recall.

    """,

    "Volume Rendering":
    """
    The Volume Rendering module allows you to visualize 3D image volumes (like CT or MRI) as translucent, realistic 3D renderings—without requiring segmentation or surface modeling. It's ideal for quick inspection, teaching, planning, or high-quality visualization of anatomy or pathology.

    🧰 Main Features:

    * Enable Volume Rendering:

        * Instantly render any scalar volume (e.g., CT scan) in 3D with just one click.

        * Shows organs, bones, and soft tissues in 3D directly from voxel data.

    * Presets:

        * Choose from predefined presets optimized for different scan types:

        * CT-Bone, CT-Soft-Tissue, CT-Cardiac, MR-Default, etc.

        * Presets control opacity and color transfer functions for realistic display.

    * Adjust Opacity & Color Mapping:

        * Manually fine-tune opacity and color transfer functions to highlight specific tissues (e.g., lung, brain, vessels).

        * Set thresholds to isolate tissue ranges (e.g., bone vs. soft tissue).

    * Rendering Techniques:

        * Choose between different backends:

            * VTK GPU Ray Casting (default)

            * VTK CPU Ray Casting

            * OSPRay Pathtracing (for photorealistic rendering, if enabled)

        * Adjust quality/performance tradeoffs as needed.

    * Cropping with ROI:

        * Use a 3D Region of Interest (ROI box) to crop the rendered volume and focus on areas of interest.

        * Crop interactively using mouse handles.

    * Shading Options:

        * Toggle surface shading and lighting for more realistic effects.

        * Control ambient, diffuse, and specular lighting properties.

    🧠 Typical Use Cases:

    * Visualizing bone fractures, tumors, or vascular structures in 3D.

    * Fast 3D preview of volumes without segmentation.

    * Creating publication-quality images and clinical presentations.

    * Teaching anatomy and demonstrating cross-sectional imaging.

    * Inspecting multimodal registrations with overlaid volumes.

    🔗 Works Well With:

    * View Controllers: Sync volume rendering with slice positions.

    * Segment Editor: Combine rendered volume with 3D segments.

    * Transforms: Move or reorient volume rendering along with data.

    * Scene Views: Save exact rendering appearance for later viewing.

    """,

    "Volumes": 
    """
    The Volumes module is the primary tool for viewing, inspecting, and adjusting scalar or labelmap volumes in 3D Slicer. A “volume” typically refers to a 3D medical image, such as a CT, MRI, or PET scan, but it can also represent segmentation maps, masks, or any voxel-based data.

    🧰 Main Features:

    * Volume Display Settings:

        * Adjust window/level (brightness and contrast) to enhance visibility of structures.

        * Apply color maps (e.g., grayscale, rainbow, labels).

        * Choose interpolation mode (smooth vs. nearest neighbor display).

        * Enable or disable volume rendering preview from the slice views.

    * Volume Information:

        * Inspect voxel dimensions, spacing, orientation, size, and data type.

        * See statistics like min/max/mean values.

        * View coordinate system and scan origin.

    * Labelmap vs. Scalar Volumes:

        * Scalar volumes store continuous data (e.g., CT intensity).

        * Labelmaps store discrete values (e.g., segment IDs).

    * Resampling and Parent Transform:

        * Check or apply transforms to volumes (e.g., from registration).

        * View or modify alignment with other objects in the scene.

    * Volume Export and Conversion:

        * Convert labelmaps to segmentation nodes or models.

        * Export volumes to standard formats (NRRD, NIfTI, etc.).

    * Volume Centering:

        * Use "Center volume" to bring a misaligned volume into the field of view.

    🧠 Typical Use Cases:

    * Loading and visualizing medical image datasets (e.g., DICOM, NRRD, NIfTI).

    * Adjusting visualization to better see anatomy (e.g., tumor, organ boundaries).

    * Viewing metadata to understand image resolution and acquisition parameters.

    * Preparing input data for segmentation or registration.

    🔗 Works Closely With:

    * Data module: Organizes and selects loaded volumes.

    * Segment Editor: Uses scalar volumes as input for segmentation.

    * Transforms: Aligns volumes with other datasets.

    * Volume Rendering: For 3D visualization of scalar volumes.

    * DICOM module: Imports volumes from clinical imaging archives.

    """,
}