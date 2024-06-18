import streamlit as st
import requests

# Function to extract email from the Cloudflare Zero Trust token


def get_user_email():
    try:
        # Extract token from headers
        token = st.request.headers.get("Cf-Access-Jwt-Assertion")
        if not token:
            return None

        # Decode token to extract user information
        # (This is a simplified example, in a real app you might want to verify the token properly)
        token_payload = requests.get(
            "https://YOUR_DOMAIN.cloudflareaccess.com/cdn-cgi/access/get-identity",
            headers={"cf-access-jwt-assertion": token}
        ).json()

        return token_payload.get("email", "No email found")
    except Exception as e:
        st.error(f"Error extracting user email: {e}")
        return None

# Streamlit app


def main():
    st.title("User Email via Cloudflare Zero Trust")
    user_email = get_user_email()
    if user_email:
        st.write(f"Authenticated user's email: **{user_email}**")
    else:
        st.write("User is not authenticated.")


if __name__ == "__main__":
    main()
