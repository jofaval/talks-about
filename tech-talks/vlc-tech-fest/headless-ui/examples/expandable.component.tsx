import { createContext, FC, ReactNode, useContext } from "react";

export type ExpandableStatus = "collapsed" | "expanded" | "none";

export type ExpandableContextProps = {
  collapse: () => void;
  expand: () => void;
  status: ExpandableStatus;
};

const context = createContext<ExpandableContextProps | undefined>(undefined);

export const useExpandableContext = () => {
  const value = useContext(context);
  if (!value) throw new Error("This should be inside <Expandable />");

  return value;
};

export type ElementChildrenProps = {
  onClick: () => void;
  active: boolean;
};

export type ElementProps = {
  children: (props: ElementChildrenProps) => ReactNode;
};

const Collapse: FC<ElementProps> = ({ children }) => {
  const { status, collapse } = useExpandableContext();
  return children({ onClick: collapse, active: status !== "collapsed" });
};

const Expand: FC<ElementProps> = ({ children }) => {
  const { status, expand } = useExpandableContext();
  return children({ onClick: expand, active: status !== "expanded" });
};

export type ExpandableProps = {
  children: ReactNode;
} & ExpandableContextProps;

const ExpandableRoot: FC<ExpandableProps> = ({ children, ...props }) => {
  return <context.Provider value={props}>{children}</context.Provider>;
};

const Expandable = Object.assign(ExpandableRoot, {
  Collapse,
  Expand,
});

export default Expandable;

const UseCase = () => {
  return (
    <Expandable>
      <Expandable.Collapse>
        {({ onClick, active }) => (
          <button disabled={!active} onClick={onClick}>
            Collapse
          </button>
        )}
      </Expandable.Collapse>

      <Expandable.Expand>
        {({ onClick, active }) => (
          <button disabled={!active} onClick={onClick}>
            Expand
          </button>
        )}
      </Expandable.Expand>
    </Expandable>
  );
};
