import React, { useEffect, useState } from "react";

type ImageProps = {
  loadingPlaceholder?: React.ReactElement;
  brokenPlaceholder?: React.ReactElement;
  url: string;
  className: string;
};

const Image: React.VFC<ImageProps> = ({ url, className = "" }) => {
  let [loadState, setLoadState] = useState("initial");

  useEffect(() => {
    setLoadState("loading");
  }, [url]);
  return (
    <div className="is-flex has-background-grey-lighter is-justify-content-center is-align-items-center is-rounded is-fullheight">
      {loadState == "error" && <span>😵</span>}
      {loadState == "loading" && (
        <progress
          className="progress is-small is-primary is-align-self-flex-start"
          max="100"
        >
          15%
        </progress>
      )}
      <img
        className={`${
          loadState !== "done" ? "is-hidden" : ""
        } ${className} is-inline-block`}
        src={url}
        alt="Image"
        onLoad={() => {
          setLoadState("done");
        }}
        onError={() => {
          setLoadState("error");
        }}
      />
    </div>
  );
};

export default Image;
