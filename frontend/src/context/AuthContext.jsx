import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";


// =========================
// CONTEXT
// =========================
const AuthContext =
  createContext();


// =========================
// PROVIDER
// =========================
export function AuthProvider({
  children,
}) {

  const [
    token,
    setToken,
  ] = useState(
    localStorage.getItem(
      "token"
    ) || null
  );

  const [
    user,
    setUser,
  ] = useState(

    JSON.parse(
      localStorage.getItem(
        "user"
      ) || "null"
    )
  );

  // =========================
  // LOGIN
  // =========================
  const login = (
    tokenValue,
    userData
  ) => {

    localStorage.setItem(
      "token",
      tokenValue
    );

    localStorage.setItem(
      "user",
      JSON.stringify(
        userData
      )
    );

    setToken(tokenValue);

    setUser(userData);
  };

  // =========================
  // LOGOUT
  // =========================
  const logout = () => {

    localStorage.removeItem(
      "token"
    );

    localStorage.removeItem(
      "user"
    );

    setToken(null);

    setUser(null);
  };

  return (

    <AuthContext.Provider
      value={{

        token,

        user,

        login,

        logout,

        isAuthenticated:
          !!token,
      }}
    >

      {children}

    </AuthContext.Provider>
  );
}


// =========================
// HOOK
// =========================
export function useAuth() {

  return useContext(
    AuthContext
  );
}