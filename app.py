import streamlit as st
from utils.ocr_processor import process_image_and_extract
from utils.ai_processor import process_text_with_ai
from utils.file_export import export_txt, export_csv
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Scribble to Digital",
    page_icon="✍️",
    layout="wide"
)

# -----------------------------
# CENTERED TITLE
# -----------------------------

st.markdown(
    "<h1 style='text-align:center;'>✍️ Scribble to Digital</h1>",
    unsafe_allow_html=True
)

st.markdown(
"""
<p style='text-align:center;font-size:18px;'>
Convert messy handwritten notes into <b>clean digital text</b> and
<b>structured to-do lists</b> using OCR and AI.
</p>
""",
unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# FEATURE CARDS
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📤 Upload Notes")
    st.write("Upload handwritten images (JPG, PNG, JPEG)")
    st.write("Instant preview")

with col2:
    st.subheader("🧠 Smart Correction")
    st.write("Fix spelling mistakes")
    st.write("Improve grammar and readability")

with col3:
    st.subheader("✅ To-Do Extraction")
    st.write("Identify action items")
    st.write("Generate structured task list")

st.markdown("---")

# -----------------------------
# IMAGE UPLOAD SECTION
# -----------------------------

st.header("📄 Handwritten Notes Processing")

uploaded_file = st.file_uploader(
    "Upload Handwritten Notes Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# IMAGE PREVIEW
# -----------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(image, width=400)

# -----------------------------
# BUTTONS
# -----------------------------

col1, col2 = st.columns(2)

convert_button = col1.button("🚀 Convert")
reset_button = col2.button("🔄 Reset")

# -----------------------------
# RESET FUNCTION
# -----------------------------

if reset_button:
    st.rerun()

# -----------------------------
# PROCESS IMAGE
# -----------------------------

if convert_button:

    if uploaded_file is None:
        st.warning("Please upload an image first.")

    else:

        with st.spinner("Processing handwritten notes..."):

            # OCR Processing
            ocr_text, error = process_image_and_extract(uploaded_file)

            if error:
                st.error(f"OCR Error: {error}")

            else:

                # -----------------------------
                # RAW OCR TEXT
                # -----------------------------

                st.markdown("---")
                st.subheader("📜 Raw OCR Text")

                st.text_area(
                    "Extracted Text",
                    ocr_text,
                    height=200
                )

                # -----------------------------
                # AI PROCESSING
                # -----------------------------

                clean_text, tasks = process_text_with_ai(ocr_text)

                # -----------------------------
                # CLEAN DIGITAL NOTES
                # -----------------------------

                st.markdown("---")
                st.subheader("📝 Clean Digital Notes")

                st.write(clean_text)

                # -----------------------------
                # TASK EXTRACTION
                # -----------------------------

                st.markdown("---")
                st.subheader("📋 Extracted To-Do Tasks")

                if tasks:

                    for task in tasks:
                        st.write(f"• {task}")

                else:
                    st.info("No tasks detected")

                # -----------------------------
                # EXPORT FILES
                # -----------------------------

                txt_file = export_txt(clean_text)
                csv_file = export_csv(tasks)

                st.markdown("---")
                st.subheader("⬇ Download Results")

                with open(txt_file, "rb") as f:
                    st.download_button(
                        label="Download Notes (TXT)",
                        data=f,
                        file_name="notes.txt",
                        mime="text/plain"
                    )

                with open(csv_file, "rb") as f:
                    st.download_button(
                        label="Download Tasks (CSV)",
                        data=f,
                        file_name="tasks.csv",
                        mime="text/csv"
                    )

                st.success("Processing completed successfully!")