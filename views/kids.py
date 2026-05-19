import streamlit as st

from streamlit_webrtc import (
    webrtc_streamer,
    WebRtcMode,
)

from src.kids_processor import (
    KidsWritingProcessor
)


def render_kids():

    st.title("🌈 Kids Learning Zone!")

    st.write(
        "Practice letters and numbers with AI"
    )

    # =====================================
    # LETTERS
    # =====================================

    st.subheader("Pick a Letter")

    letter_cols = st.columns(7)

    for idx, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):

        if letter_cols[idx % 7].button(letter):

            st.session_state.target_character = (
                letter
            )

            st.session_state.mode = (
                "emnist_letters"
            )

    # =====================================
    # DIGITS
    # =====================================

    st.subheader("Pick a Digit")

    digit_cols = st.columns(5)

    for idx in range(10):

        if digit_cols[idx % 5].button(str(idx)):

            st.session_state.target_character = (
                str(idx)
            )

            st.session_state.mode = "mnist"

    # SHOW TARGET
    target = st.session_state.get(
        "target_character"
    )
    mode = st.session_state.get(
        "mode"
    )

    if target:

        st.subheader(
            f"Practice: {target}"
        )

        ctx = webrtc_streamer(

            key="kids-learning",

            mode=WebRtcMode.SENDRECV,

            video_processor_factory=lambda:
                KidsWritingProcessor(
                    target_character=target,
                    dataset_name=mode,
                ),

            media_stream_constraints={
                "video": True,
                "audio": False,
            },

            async_processing=True,
        )

        if ctx.video_processor:

            col1, col2 = st.columns(2)

            with col1:

                if st.button("✅ Check"):

                    ctx.video_processor.check_answer()

            with col2:

                if st.button("🧹 Clear"):

                    ctx.video_processor.clear_canvas()

            if ctx.video_processor.last_prediction:

                st.write(
                    f"Predicted: "
                    f"{ctx.video_processor.last_prediction}"
                )

            if ctx.video_processor.result_message:

                if "Well done" in (
                    ctx.video_processor.result_message
                ):

                    st.success(
                        ctx.video_processor.result_message
                    )

                else:

                    st.warning(
                        ctx.video_processor.result_message
                    )