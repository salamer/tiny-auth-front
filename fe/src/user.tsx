import { useUser } from "@clerk/clerk-react";
 
export default function User() {
  const { isLoaded, isSignedIn, user } = useUser();
 
  if (!isLoaded || !isSignedIn) {
    return null;
  }
 
  return <div>Hello, {user.firstName} welcome to Clerk</div>;
}