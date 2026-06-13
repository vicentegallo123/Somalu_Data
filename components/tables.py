import streamlit as st


class Tables:

    @staticmethod
    def show(df):

        df = df.copy()

        if "DESCRIPCION" in df.columns:
            df["DESCRIPCION"] = (
                df["DESCRIPCION"]
                .fillna("")
                .astype(str)
            )

        st.dataframe(
            df,
            width="stretch"
        )

    @staticmethod
    def top_productos(df):

        df = df.copy()

        if "DESCRIPCION" in df.columns:
            df["DESCRIPCION"] = (
                df["DESCRIPCION"]
                .fillna("")
                .astype(str)
            )

        st.dataframe(
            df.head(20),
            width="stretch"
        )

    @staticmethod
    def descuentos(df):

        df = df.copy()

        st.dataframe(
            df,
            width="stretch"
        )